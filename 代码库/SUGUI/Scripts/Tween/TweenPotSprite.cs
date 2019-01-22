//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEngine.UI;
using XPlugin;

/// <summary>
/// 透明度补间
/// </summary>

[AddComponentMenu("SUGUI/Tween/Tween PotSprite")]
public class TweenPotSprite : UITweener {
#if UNITY_3_5
	public float from = 1f;
	public float to = 1f;
#else
	[Range(0f, 1f)]
	public float from = 1f;
	[Range(0f, 1f)]
	public float to = 1f;
#endif
	ImageEffectOpaque dd;
	PotSprite mPotSprite;
	Color mColor;

	public PotSprite CachedPotSprite {
		get {
			if (mPotSprite == null)
			{
				mPotSprite = GetComponent<PotSprite>();
				if (mPotSprite == null) mPotSprite = GetComponentInChildren<PotSprite>();
			}
			mColor = mPotSprite.Color;
			return mPotSprite;
		}
	}

	public float value {
		get {
			return alpha;
		}
		set {
			alpha = value;
		}
	}

	/// <summary>
	/// 当 alpha 等于 0 时，关闭 SpriteRenderer的渲染，减少透支
	/// </summary>
	public bool AutoDisableByAlpha = true;

	public float alpha {
		get {
			return CachedPotSprite.Color.a;
		}
		set {
			CachedPotSprite.Color = new Color(mColor.r, mColor.g, mColor.b, value);

			if (AutoDisableByAlpha)
			{
				if (value <= 0 && CachedPotSprite.enabled)
				{
					CachedPotSprite.enabled = false;
				} else if (value > 0 && !CachedPotSprite.enabled)
				{
					CachedPotSprite.enabled = true;
				}
			}
		}
	}

	protected override void OnUpdate(float factor, bool isFinished) { value = Mathf.Lerp(from, to, factor); }

	/// <summary>
	/// 开始补间操作
	/// </summary>

	static public TweenPotSprite Begin(GameObject go, float duration, float alpha) {
		TweenPotSprite comp = UITweener.Begin<TweenPotSprite>(go, duration);
		comp.from = comp.value;
		comp.to = alpha;

		if (duration <= 0f)
		{
			comp.Sample(1f, true);
			comp.enabled = false;
		}
		return comp;
	}

	public override void SetStartToCurrentValue() { from = value; }
	public override void SetEndToCurrentValue() { to = value; }
}
