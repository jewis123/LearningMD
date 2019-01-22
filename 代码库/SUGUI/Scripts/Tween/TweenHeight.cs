//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;

/// <summary>
/// 补间Height
/// </summary>

[RequireComponent(typeof(RectTransform))]
[AddComponentMenu("SUGUI/Tween/Tween Height")]
public class TweenHeight : UITweener
{
	public int from = 100;
	public int to = 100;
	public bool updateTable = false;

    RectTransform mRectTransform;

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
            return (int)cachedWidget.sizeDelta.y; 
        } 
        set 
        {
            cachedWidget.sizeDelta = new Vector2(cachedWidget.sizeDelta.x, value); 
        } 
    }

	protected override void OnUpdate (float factor, bool isFinished)
	{
		value = Mathf.RoundToInt(from * (1f - factor) + to * factor);
	}

	/// <summary>
    /// 开始补间操作
	/// </summary>
    static public TweenHeight Begin(RectTransform rectTransform, float duration, int height)
	{
        TweenHeight comp = UITweener.Begin<TweenHeight>(rectTransform.gameObject, duration);
        comp.from = (int)rectTransform.sizeDelta.y;
		comp.to = height;

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
