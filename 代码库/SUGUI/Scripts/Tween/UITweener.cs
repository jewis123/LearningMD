//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// 所有补间操作的基类
/// </summary>
public abstract class UITweener : MonoBehaviour {
	/// <summary>
	/// 当前的补间动画触发回调函数。
	/// </summary>
	static public UITweener current;

	public EaseType easeType = EaseType.linear;
	[HideInInspector]
	public Style style = Style.Once;

	/// <summary>
	/// 动画曲线
	/// </summary>
	[HideInInspector]
	public AnimationCurve animationCurve = new AnimationCurve (new Keyframe (0f, 0f, 0f, 1f), new Keyframe (1f, 1f, 1f, 0f));

	public enum Style {
		Once,
		Loop,
		PingPong,
	}
	/// <summary>
	/// 补间是否忽略时标
	/// </summary>

	[HideInInspector]
	public bool ignoreTimeScale = true;

	/// <summary>
	/// 延迟
	/// </summary>

	[HideInInspector]
	public float delay = 0f;

	/// <summary>
	/// 补间时常
	/// </summary>

	public float duration = 1f;

	/// <summary>
	/// 是否使用较陡的曲线 便于in/out风格插值。
	/// </summary>

	[HideInInspector]
	public bool steeperCurves = false;

	/// <summary>
	/// 补间序列
	/// </summary>

	[HideInInspector]
	public int tweenGroup = 0;

	/// <summary>
	/// 动画结束时回调
	/// </summary>

	[HideInInspector]
	public List<EventDelegate> onFinished = new List<EventDelegate> ();

	bool mStarted = false;
	float mStartTime = 0f;
	float mDuration = 0f;
	float mAmountPerDelta = 1000f;
	float mFactor = 0f;

	/// <summary>
	/// 每次增量
	/// </summary>

	public float amountPerDelta {
		get {
			if (mDuration != duration) {
				mDuration = duration;
				mAmountPerDelta = Mathf.Abs ((duration > 0f) ? 1f / duration : 1000f) * Mathf.Sign (mAmountPerDelta);
			}
			return mAmountPerDelta;
		}
	}

	/// <summary>
	/// 补间因子，0-1
	/// </summary>

	public float tweenFactor { get { return mFactor; } set { mFactor = Mathf.Clamp01 (value); } }

	/// <summary>
	/// Direction that the tween is currently playing in.
	/// 当前使用的补间动画
	/// </summary>

	public AnimationOrTween.Direction direction { get { return amountPerDelta < 0f ? AnimationOrTween.Direction.Reverse : AnimationOrTween.Direction.Forward; } }

	/// <summary>
	/// 添加组件时自动重置.
	/// </summary>
	void Reset () {
		if (!mStarted) {
			SetStartToCurrentValue ();
			SetEndToCurrentValue ();
		}
	}

	protected virtual void Start () { Update (); }

	void Update () {
		float delta = ignoreTimeScale ? RealTime.deltaTime : Time.deltaTime;
		float time = ignoreTimeScale ? RealTime.time : Time.time;

		if (!mStarted) {
			mStarted = true;
			mStartTime = time + delay;
		}

		if (time < mStartTime) return;

		mFactor += amountPerDelta * delta;

		if (style == Style.Loop) {
			if (mFactor > 1f) {
				mFactor -= Mathf.Floor (mFactor);
			}
		} else if (style == Style.PingPong) {
			if (mFactor > 1f) {
				mFactor = 1f - (mFactor - Mathf.Floor (mFactor));
				mAmountPerDelta = -mAmountPerDelta;
			} else if (mFactor < 0f) {
				mFactor = -mFactor;
				mFactor -= Mathf.Floor (mFactor);
				mAmountPerDelta = -mAmountPerDelta;
			}
		}

		if ((style == Style.Once) && (duration == 0f || mFactor > 1f || mFactor < 0f)) {
			mFactor = Mathf.Clamp01 (mFactor);
			Sample (mFactor, true);

			if (duration == 0f || (mFactor == 1f && mAmountPerDelta > 0f || mFactor == 0f && mAmountPerDelta < 0f))
				enabled = false;

			if (current == null) {
				current = this;

				if (onFinished != null) {
					mTemp = onFinished;
					onFinished = new List<EventDelegate> ();

					EventDelegate.Execute (mTemp);

					for (int i = 0; i < mTemp.Count; ++i) {
						EventDelegate ed = mTemp[i];
						if (ed != null) EventDelegate.Add (onFinished, ed, ed.oneShot);
					}
					mTemp = null;
				}

				current = null;
			}
		} else Sample (mFactor, false);
	}

	List<EventDelegate> mTemp = null;

	/// <summary>
	/// 设置一个新的委托事件
	/// </summary>

	public void SetOnFinished (EventDelegate.Callback del) { EventDelegate.Set (onFinished, del); }

	/// <summary>
	/// 设置一个新的委托事件
	/// </summary>

	public void SetOnFinished (EventDelegate del) { EventDelegate.Set (onFinished, del); }

	/// <summary>
	/// 添加新的委托.
	/// </summary>

	public void AddOnFinished (EventDelegate.Callback del) { EventDelegate.Add (onFinished, del); }

	/// <summary>
	/// 添加新的委托
	/// </summary>

	public void AddOnFinished (EventDelegate del) { EventDelegate.Add (onFinished, del); }

	/// <summary>
	/// 移除委托
	/// </summary>

	public void RemoveOnFinished (EventDelegate del) {
		if (onFinished != null) onFinished.Remove (del);
		if (mTemp != null) mTemp.Remove (del);
	}

	/// <summary>
	/// 标记为未启动
	/// </summary>

	void OnDisable () { mStarted = false; }

	/// <summary>
	/// 在指定因素采样补间动画
	/// </summary>

	public void Sample (float factor, bool isFinished) {
		float val = Mathf.Clamp01 (factor);
		val = EaseManager.EasingFromType (0, 1, val, easeType);
		// Add animationCurve By sxb
		OnUpdate ((animationCurve != null) ? animationCurve.Evaluate (val) : val, isFinished);
		//OnUpdate(val, isFinished);
	}

	/// <summary>
	/// 反弹逻辑
	/// </summary>

	float BounceLogic (float val) {
		if (val < 0.363636f) // 0.363636 = (1/ 2.75)
		{
			val = 7.5685f * val * val;
		} else if (val < 0.727272f) // 0.727272 = (2 / 2.75)
		{
			val = 7.5625f * (val -= 0.545454f) * val + 0.75f; // 0.545454f = (1.5 / 2.75) 
		} else if (val < 0.909090f) // 0.909090 = (2.5 / 2.75) 
		{
			val = 7.5625f * (val -= 0.818181f) * val + 0.9375f; // 0.818181 = (2.25 / 2.75) 
		} else {
			val = 7.5625f * (val -= 0.9545454f) * val + 0.984375f; // 0.9545454 = (2.625 / 2.75) 
		}
		return val;
	}

	/// <summary>
	/// 正向播放
	/// </summary>

	public void PlayForward () { Play (true); }

	/// <summary>
	/// 反向播放
	/// </summary>

	public void PlayReverse () { Play (false); }

	///<summery>
	///重新播放
	///</summery>
	public void RePlay () {
		ResetToBeginning ();
		PlayForward ();
	}

	/// <summary>
	/// 播放补间
	/// </summary>

	public void Play (bool forward) {
		mAmountPerDelta = Mathf.Abs (amountPerDelta);
		if (!forward) mAmountPerDelta = -mAmountPerDelta;
		enabled = true;
		Update ();
	}

	/// <summary>
	/// 复位补间动画
	/// </summary>

	public void ResetToBeginning () {
		mStarted = false;
		mFactor = (amountPerDelta < 0f) ? 1f : 0f;
		Sample (mFactor, false);
	}

	/// <summary>
	/// 反转补间动画方向
	/// </summary>

	public void Toggle () {
		if (mFactor > 0f) {
			mAmountPerDelta = -amountPerDelta;
		} else {
			mAmountPerDelta = Mathf.Abs (amountPerDelta);
		}
		enabled = true;
	}

	/// <summary>
	/// 实际补间的逻辑-继承
	/// </summary>

	abstract protected void OnUpdate (float factor, bool isFinished);

	/// <summary>
	/// 开始补间操作
	/// </summary>

	static public T Begin<T> (GameObject go, float duration) where T : UITweener {
		T comp = go.GetComponent<T> ();
#if UNITY_FLASH
		if ((object) comp == null) comp = (T) go.AddComponent<T> ();
#else
		//找到未设置id组的补间
		if (comp != null && comp.tweenGroup != 0) {
			comp = null;
			T[] comps = go.GetComponents<T> ();
			for (int i = 0, imax = comps.Length; i < imax; ++i) {
				comp = comps[i];
				if (comp != null && comp.tweenGroup == 0) break;
				comp = null;
			}
		}

		if (comp == null) comp = go.AddComponent<T> ();
#endif
		comp.mStarted = false;
		comp.duration = duration;
		comp.mFactor = 0f;
		comp.mAmountPerDelta = Mathf.Abs (comp.amountPerDelta);
		comp.style = Style.Once;
		comp.animationCurve = new AnimationCurve (new Keyframe (0f, 0f, 0f, 1f), new Keyframe (1f, 1f, 1f, 0f));
		comp.enabled = true;

		if (duration <= 0f) {
			comp.Sample (1f, true);
			comp.enabled = false;
		}
		return comp;
	}

	/// <summary>
	/// 设置开始(form)值
	/// </summary>

	public virtual void SetStartToCurrentValue () { }

	/// <summary>
	/// 设置结束(to)值
	/// </summary>
	public virtual void SetEndToCurrentValue () { }
}