//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEngine.EventSystems;

/// <summary>
/// 按钮事件大小缩放
/// </summary>

[AddComponentMenu("SUGUI/Interaction/Button Scale")]
public class UIButtonScale : MonoBehaviour, SUGUIEventSystemsInterface
{
    public Transform tweenTarget;
	public Vector3 hover = new Vector3(1.05f, 1.05f, 1.05f);
	public Vector3 pressed = new Vector3(0.95f, 0.95f, 0.95f);
    public float duration = 0.2f;

    Vector3 mScale;

    bool mStarted = false;

    void Start()
    {
        if (!mStarted)
        {
            mStarted = true;
            if (tweenTarget == null) tweenTarget = transform;
            mScale = tweenTarget.localScale;
        }
    }

    void OnDisable()
    {
        if (mStarted && tweenTarget != null)
        {
            TweenScale tc = tweenTarget.GetComponent<TweenScale>();

            if (tc != null)
            {
                tc.value = mScale;
                tc.enabled = false;
            }
        }
    }

    public void OnPointerEnter(PointerEventData eventData)
    {
        Scale(hover);
    }

    public void OnPointerExit(PointerEventData eventData)
    {
        Scale(mScale);
    }

    public void OnPointerDown(PointerEventData eventData)
    {
        Scale(pressed);
    }

    public void OnPointerUp(PointerEventData eventData)
    {
        Scale(mScale);
    }

    public void OnPointerClick(PointerEventData eventData)
    {
    }

    void Scale(Vector3 to)
    {
        TweenScale.Begin(tweenTarget.gameObject,duration ,to ).easeType = EaseType.linear;
    }
}
