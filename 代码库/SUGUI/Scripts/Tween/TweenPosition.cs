//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;

/// <summary>
/// 坐标补间
/// </summary>

[AddComponentMenu("SUGUI/Tween/Tween Position")]
public class TweenPosition : UITweener
{
	public Vector3 from;
	public Vector3 to;

    /// <summary>
    /// 是否是世界坐标
    /// </summary>
	[HideInInspector]
	public bool worldSpace = false;
    /// <summary>
    /// 是否有ugui
    /// </summary>
    public bool notUGUI = false;
    RectTransform mRectTransform;

    public Transform cachedTransform 
    { 
        get 
        {
            if (!notUGUI)
            {
                if (mRectTransform == null)
                {
                    mRectTransform = gameObject.GetComponent<RectTransform>();
                    if(mRectTransform == null)
                    {
                        notUGUI = true;
                        return transform;
                    }
                }
                return mRectTransform;
            }
            else
            {
                return transform;
            }
        } 
    }
	public Vector3 value
	{
		get
		{
			return worldSpace ? cachedTransform.position : cachedTransform.localPosition;
		}
		set
		{
            if (worldSpace) cachedTransform.position = value;
            else cachedTransform.localPosition = value;

        }
	}

	void Awake () 
    {
        mRectTransform = GetComponent<RectTransform>();
        if (mRectTransform == null) notUGUI = true;
    }


	protected override void OnUpdate (float factor, bool isFinished) 
    { 
        value = from * (1f - factor) + to * factor; 
    }

	/// <summary>
	/// 开始补间操作
	/// </summary>

	static public TweenPosition Begin (GameObject go, float duration, Vector3 pos)
	{
		TweenPosition comp = UITweener.Begin<TweenPosition>(go, duration);
		comp.from = comp.value;
		comp.to = pos;

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
