using UnityEngine;
using System.Collections;
using System;
using UnityEngine.UI;

[AddComponentMenu("SUGUI/Tween/Tween LayoutElement")]
[RequireComponent(typeof(LayoutElement))]
public class TweenLayoutElement : UITweener
{
    public float from, to;
    public bool horizontal;

    private LayoutElement layoutElement;

    public float value
    {
        get
        {
            if (layoutElement == null)
            {
                layoutElement = GetComponent<LayoutElement>();
            }
            return horizontal ? layoutElement.minWidth : layoutElement.minHeight;
        }
        set
        {
            if (layoutElement == null)
            {
                layoutElement = GetComponent<LayoutElement>();
            }
            if (horizontal)
            {
                layoutElement.minWidth = layoutElement.preferredWidth = value;
            }
            else
            {
                layoutElement.minHeight = layoutElement.preferredHeight = value;
            }
        }
    }

    protected override void OnUpdate(float factor, bool isFinished)
    {
        value = Mathf.Lerp(from, to, factor);
    }

    public void ResetToRestart(bool resetToStart)
    {
        tweenFactor = resetToStart ? 0f : 1f;
        Sample(tweenFactor, false);
    }

    [ContextMenu("设置当前值为From的值")]
    public override void SetStartToCurrentValue() { from = value; }

    [ContextMenu("设置当前值为To的值")]
    public override void SetEndToCurrentValue() { to = value; }

    [ContextMenu("切换到From值状态")]
    public void SetCurrentValueToStart() { value = from; }

    [ContextMenu("切换到To值状态")]
    public void SetCurrentValueToEnd() { value = to; }
}
