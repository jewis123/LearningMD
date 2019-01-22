//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;

/// <summary>
/// Tween the object's local scale.
/// </summary>

[AddComponentMenu("SUGUI/Tween/Tween Scale")]
public class TweenScale : UITweener
{
	public Vector3 from = Vector3.one;
	public Vector3 to = Vector3.one;
	public bool updateTable = false;

	Transform mTrans;
	//UITable mTable;

    public Transform cachedTransform
    {
        get
        {
            if (mTrans == null)
                mTrans = transform;
            return mTrans;
        }
    }

	public Vector3 value 
    { 
        get 
        { 
            return cachedTransform.localScale; 
        } 
        set 
        { 
            cachedTransform.localScale = value; 
        } 
    }

	protected override void OnUpdate (float factor, bool isFinished)
	{
		value = from * (1f - factor) + to * factor;

        //if (updateTable)
        //{
        //    if (mTable == null)
        //    {
        //        mTable = NGUITools.FindInParents<UITable>(gameObject);
        //        if (mTable == null) { updateTable = false; return; }
        //    }
        //    mTable.repositionNow = true;
        //}
	}

	/// <summary>
	/// 开始补间操作
	/// </summary>
	static public TweenScale Begin (GameObject go, float duration, Vector3 scale)
	{
		TweenScale comp = UITweener.Begin<TweenScale>(go, duration);
		comp.from = comp.value;
		comp.to = scale;

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
	public void SetCurrentValueToStart () { value = from; }

	[ContextMenu("切换到To值状态")]
	public void SetCurrentValueToEnd () { value = to; }
}
