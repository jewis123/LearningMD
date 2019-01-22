//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEngine.EventSystems;
/// <summary>
/// Simple example script of how a button can be offset visibly when the mouse hovers over it or it gets pressed.
/// </summary>

[AddComponentMenu("SUGUI/Interaction/Button Offset")]
public class UIButtonOffset : MonoBehaviour, SUGUIEventSystemsInterface
{
	public Transform tweenTarget;
	public Vector3 hover = Vector3.zero;
	public Vector3 pressed = new Vector3(2f, -2f);
	public float duration = 0.2f;

	Vector3 mPos;
	bool mStarted = false;

	void Start ()
	{
		if (!mStarted)
		{
			mStarted = true;
			if (tweenTarget == null) tweenTarget = transform;
			mPos = tweenTarget.localPosition;
		}
	}

    void OnDisable()
    {
        if (mStarted && tweenTarget != null)
        {
            TweenPosition tc = tweenTarget.GetComponent<TweenPosition>();

            if (tc != null)
            {
                tc.value = mPos;
                tc.enabled = false;
            }
        }
    }


    public void OnPointerEnter(PointerEventData eventData)
    {
        Offset(mPos + hover);
    }

    public void OnPointerExit(PointerEventData eventData)
    {
        Offset(mPos);
    }

    public void OnPointerDown(PointerEventData eventData)
    {
        Offset(mPos + pressed);
    }

    public void OnPointerUp(PointerEventData eventData)
    {
        Offset(mPos);
    }

    public void OnPointerClick(PointerEventData eventData)
    {
    }

    void Offset(Vector3 to)
    {
        TweenPosition.Begin(tweenTarget.gameObject, duration, to).easeType = EaseType.linear;
    }
}
