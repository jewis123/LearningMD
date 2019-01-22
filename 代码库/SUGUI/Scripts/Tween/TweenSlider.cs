//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

/// <summary>
/// 进度条补间 （可以用于经验值改变动画等）
/// </summary>
[RequireComponent(typeof(Slider))]
[AddComponentMenu("SUGUI/Tween/Tween Slider")]
public class TweenSlider : UITweener
{

    public float from;
    public float to;
    public bool NeedCarry = false;


    private Slider mSlider;
    public Slider cacheSlider
    {
        get
        {
            mSlider = GetComponent<Slider>();
            if (mSlider == null)
            {
                Debug.LogError("Slider null");
            }
            return mSlider;
        }
    }

    float mValue;

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

    public float sliderValue
    {
        set
        {
            if (NeedCarry)
            {
                cacheSlider.value = (value >= 1) ? value - Mathf.Floor(value) : value;
            }
            else
            {
                cacheSlider.value = (value > 1) ? value - Mathf.Floor(value) : value;
            }
        }
    }

    protected  void ValueUpdate(float value, bool isFinished)
    {
        this.sliderValue = value;
    }

    public static TweenSlider Begin(Slider slider, float duration, float delay, float from, float to)
    {
        TweenSlider comp = UITweener.Begin<TweenSlider>(slider.gameObject, duration);
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

