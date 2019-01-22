//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

[RequireComponent(typeof(Text))]
[AddComponentMenu("SUGUI/Tween/Tween Text")]
public class TweenText : UITweener
{

    public float from;
    public float to;

    float mValue;

    private Text mText;
    public Text cacheText
    {
        get
        {
            mText = GetComponent<Text>();
            if (mText == null)
            {
                Debug.LogError("Text null");
            }
            return mText;
        }
    }

    /// <summary>
    /// 小数位
    /// </summary>
    public int digits;


    public float value
    {
        get { return mValue; }
        set
        {
            mValue = value;
        }
    }

    protected override void OnUpdate(float factor, bool isFinished)
    {
        value = from + factor * (to - from);
        ValueUpdate(value, isFinished);
    }


    protected void ValueUpdate(float value, bool isFinished)
    {
        cacheText.text = (System.Math.Round(value, digits)).ToString();
    }

    public static TweenText Begin(Text label, float duration, float delay, float from, float to)
    {
        TweenText comp = UITweener.Begin<TweenText>(label.gameObject, duration);
        comp.from = from;
        comp.to = to;
        comp.delay = delay;

        if (duration <= 0)
        {
            comp.Sample(1, true);
            comp.enabled = false;
        }
        return comp;
    }
}
