//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEngine.EventSystems;
/// <summary>
/// 激活或隐藏一个对象和子对象
/// </summary>

[AddComponentMenu("SUGUI/Interaction/Button Activate")]
public class UIButtonActivate : MonoBehaviour, SUGUIEventSystemsInterface
{
    public GameObject target;
    public bool state = true;


    public void OnPointerClick(PointerEventData eventData)
    {
        if (target != null)
            target.SetActive(state);
    }

    public void OnPointerEnter(PointerEventData eventData)
    {
    }

    public void OnPointerExit(PointerEventData eventData)
    {
    }

    public void OnPointerDown(PointerEventData eventData)
    {
    }

    public void OnPointerUp(PointerEventData eventData)
    {
    }
}