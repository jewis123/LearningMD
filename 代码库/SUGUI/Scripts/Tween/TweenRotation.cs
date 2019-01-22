//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;

/// <summary>
/// 旋转
/// </summary>

[AddComponentMenu("SUGUI/Tween/Tween Rotation")]
public class TweenRotation : UITweener
{
	public Vector3 from;
	public Vector3 to;

	Transform mTrans;

	public Transform cachedTransform 
    { 
        get 
        { 
            if (mTrans == null) 
                mTrans = transform; 
            return mTrans; 
        } 
    }

	public Quaternion value 
    { 
        get 
        { 
            return cachedTransform.localRotation; 
        } 
        set 
        { 
            cachedTransform.localRotation = value; 
        } 
    }

	protected override void OnUpdate (float factor, bool isFinished)
	{
		value = Quaternion.Euler(new Vector3(
			Mathf.Lerp(from.x, to.x, factor),
			Mathf.Lerp(from.y, to.y, factor),
			Mathf.Lerp(from.z, to.z, factor)));
	}

	/// <summary>
	/// 开始补间操作
	/// </summary>

	static public TweenRotation Begin (GameObject go, float duration, Quaternion rot)
	{
		TweenRotation comp = UITweener.Begin<TweenRotation>(go, duration);
		comp.from = comp.value.eulerAngles;
		comp.to = rot.eulerAngles;

		if (duration <= 0f)
		{
			comp.Sample(1f, true);
			comp.enabled = false;
		}
		return comp;
	}

	[ContextMenu("设置当前值为From的值")]
	public override void SetStartToCurrentValue () { from = value.eulerAngles; }

    [ContextMenu("设置当前值为To的值")]
	public override void SetEndToCurrentValue () { to = value.eulerAngles; }

	[ContextMenu("切换到From值状态")]
	public void SetCurrentValueToStart () { value = Quaternion.Euler(from); }

    [ContextMenu("切换到To值状态")]
	public void SetCurrentValueToEnd () { value = Quaternion.Euler(to); }
}
