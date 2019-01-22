//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEngine.EventSystems;
/// <summary>
/// 按钮事件旋转
/// </summary>

[AddComponentMenu("SUGUI/Interaction/Button Rotation")]
public class UIButtonRotation : MonoBehaviour, SUGUIEventSystemsInterface
{
	public Transform tweenTarget;
	public Vector3 hover = Vector3.zero;
	public Vector3 pressed = Vector3.zero;
	public float duration = 0.2f;

	Quaternion mRot;
	bool mStarted = false;

	void Start ()
	{
		if (!mStarted)
		{
			mStarted = true;
			if (tweenTarget == null) tweenTarget = transform;
			mRot = tweenTarget.localRotation;
		}
	}
    void OnDisable()
    {
        if (mStarted && tweenTarget != null)
        {
            TweenRotation tc = tweenTarget.GetComponent<TweenRotation>();

            if (tc != null)
            {
                tc.value = mRot;
                tc.enabled = false;
            }
        }
    }

    public void OnPointerEnter(PointerEventData eventData)
    {
        Rotation(mRot * Quaternion.Euler(hover));
    }

    public void OnPointerExit(PointerEventData eventData)
    {
        Rotation(mRot);
    }

    public void OnPointerDown(PointerEventData eventData)
    {
        Rotation(mRot * Quaternion.Euler(pressed));
    }

    public void OnPointerUp(PointerEventData eventData)
    {
        Rotation(mRot);
    }

    public void OnPointerClick(PointerEventData eventData)
    {
    }

    void Rotation(Quaternion to)
    {
        TweenRotation.Begin(tweenTarget.gameObject, duration, to).easeType = EaseType.linear;
    }
}
