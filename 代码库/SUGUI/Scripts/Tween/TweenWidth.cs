//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEngine.UI;
/// <summary>
/// 补间Width
/// </summary>

[RequireComponent(typeof(RectTransform))]
[AddComponentMenu("SUGUI/Tween/Tween Width")]
public class TweenWidth : UITweener
{
	public int from = 100;
	public int to = 100;
	public bool updateTable = false;

    RectTransform mRectTransform;
	//UITable mTable;

    public RectTransform cachedWidget 
    { 
        get 
        {
            if (mRectTransform == null)
                mRectTransform = GetComponent<RectTransform>(); 
            return mRectTransform; 
        } 
        
    }



	public int value 
    { 
        get 
        { 
            return (int)cachedWidget.sizeDelta.x; 
        } 
        set 
        {
            cachedWidget.sizeDelta = new Vector2(value, cachedWidget.sizeDelta.y); 
        } 
    }

	/// <summary>
	/// Tween the value.
	/// </summary>

	protected override void OnUpdate (float factor, bool isFinished)
	{
		value = Mathf.RoundToInt(from * (1f - factor) + to * factor);

        //if (updateTable)
        //{
        //    if (mTable == null)
        //    {
        //        mTable = SUGUITools.FindInParents<UITable>(gameObject);
        //        if (mTable == null) { updateTable = false; return; }
        //    }
        //    mTable.repositionNow = true;
        //}
	}

	/// <summary>
	/// Start the tweening operation.
	/// </summary>

    static public TweenWidth Begin(RectTransform rectTransform, float duration, int width)
	{
        TweenWidth comp = UITweener.Begin<TweenWidth>(rectTransform.gameObject, duration);
        comp.from = (int)rectTransform.sizeDelta.x;
		comp.to = width;

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
