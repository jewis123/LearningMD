//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEngine.UI;

/// <summary>
/// 颜色补间
/// </summary>

[AddComponentMenu("SUGUI/Tween/Tween Color")]
public class TweenColor : UITweener
{
	public Color from = Color.white;
	public Color to = Color.white;

	bool mCached = false;
    MaskableGraphic mMaskableGraphic;
	Material mMat;
	Light mLight;

	void Cache ()
	{
		mCached = true;
        mMaskableGraphic = GetComponent<MaskableGraphic>();
        Renderer ren = gameObject.GetComponent<Renderer>();
		if (ren != null) mMat = ren.material;
		mLight = gameObject.GetComponent<Light>();
        if (mMaskableGraphic == null && mMat == null && mLight == null)
            mMaskableGraphic = GetComponentInChildren<MaskableGraphic>();
	}

	public Color value
	{
		get
		{
			if (!mCached) Cache();
            if (mMaskableGraphic != null) return mMaskableGraphic.color;
			if (mLight != null) return mLight.color;
			if (mMat != null) return mMat.color;
			return Color.black;
		}
		set
		{
			if (!mCached) Cache();
            if (mMaskableGraphic != null) mMaskableGraphic.color = value;
			if (mMat != null) mMat.color = value;

			if (mLight != null)
			{
				mLight.color = value;
				mLight.enabled = (value.r + value.g + value.b) > 0.01f;
			}
		}
	}

	protected override void OnUpdate (float factor, bool isFinished) { value = Color.Lerp(from, to, factor); }

	/// <summary>
	/// 开始补间
	/// </summary>

	static public TweenColor Begin (GameObject go, float duration, Color color)
	{
#if UNITY_EDITOR
		if (!Application.isPlaying) return null;
#endif
		TweenColor comp = UITweener.Begin<TweenColor>(go, duration);
		comp.from = comp.value;
		comp.to = color;

		if (duration <= 0f)
		{
			comp.Sample(1f, true);
			comp.enabled = false;
		}
		return comp;
	}

	[ContextMenu("设置当前值为From的值")]
	public override void SetStartToCurrentValue () { from = value; }

	[ContextMenu("设置当前值为To的值")]
	public override void SetEndToCurrentValue () { to = value; }

	[ContextMenu("切换到From值状态")]
	void SetCurrentValueToStart () { value = from; }

	[ContextMenu("切换到To值状态")]
	void SetCurrentValueToEnd () { value = to; }
}
