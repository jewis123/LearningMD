using UnityEngine;
using System.Collections;
using UnityEngine.EventSystems;

public interface SUGUIEventSystemsInterface : IPointerEnterHandler, IPointerDownHandler, IPointerClickHandler, IPointerUpHandler, IPointerExitHandler
{
    /// <summary>
    /// 悬停
    /// </summary>
    /// <param name="eventData"></param>
    new void OnPointerEnter(PointerEventData eventData);
    /// <summary>
    /// 按下
    /// </summary>
    /// <param name="eventData"></param>
    new void OnPointerDown(PointerEventData eventData);
    /// <summary>
    /// 点击
    /// </summary>
    /// <param name="eventData"></param>
    new void OnPointerClick(PointerEventData eventData);
    /// <summary>
    /// 抬起
    /// </summary>
    /// <param name="eventData"></param>
    new void OnPointerUp(PointerEventData eventData);
    /// <summary>
    /// 悬停离开
    /// </summary>
    /// <param name="eventData"></param>
    new void OnPointerExit(PointerEventData eventData);
}
