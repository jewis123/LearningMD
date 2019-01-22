//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Events;
using System.Collections;

/// <summary>
/// 根据进度条百分百设置颜色
/// </summary>
[AddComponentMenu("SUGUI/Interaction/Slider Colors")]
public class SliderColors : MonoBehaviour
{
    public Image target;
    public Color[] colors = new Color[] { Color.red, Color.yellow, Color.green };

    Slider mSlider;

    void Start()
    {
        mSlider = GetComponent<Slider>();
        if (mSlider == null)
        {
            Debug.LogError("Slider null");
            return;
        }
        if (target == null)
        {
            target = mSlider.GetComponentInChildren<Image>();
        }
        UnityAction<float> valueChange = new UnityAction<float>(OnValueChanged);
        mSlider.onValueChanged.AddListener(valueChange);
        OnValueChanged(mSlider.value);
    }

    public void OnValueChanged(float value)
    {
        float val = value * (colors.Length - 1);
        int startIndex = Mathf.FloorToInt(val);
        Color c = colors[0];
        if ((startIndex + 1) < colors.Length)
        {
            c = Color.Lerp(colors[startIndex], colors[startIndex + 1], val - startIndex);
        }
        else if (startIndex < colors.Length)
        {
            c = colors[startIndex];
        }
        target.color = c;
    }
}
