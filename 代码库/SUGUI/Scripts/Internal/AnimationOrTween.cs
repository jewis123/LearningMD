//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;

namespace AnimationOrTween
{
    /// <summary>
    /// 触发类型
    /// </summary>
	public enum Trigger
	{
		OnClick,
		OnHover,
		OnPress,
		OnHoverTrue,
		OnHoverFalse,
		OnPressTrue,
		OnPressFalse,
		OnActivate,
		OnActivateTrue,
		OnActivateFalse,
		OnDoubleClick,
		OnSelect,
		OnSelectTrue,
		OnSelectFalse,
	}

    /// <summary>
    /// 方向
    /// </summary>
	public enum Direction
	{
		Reverse = -1,
		Toggle = 0,
		Forward = 1,
	}
    /// <summary>
    /// 启用条件
    /// </summary>
	public enum EnableCondition
	{
		DoNothing = 0,
		EnableThenPlay,
	}
    /// <summary>
    /// 禁用状态
    /// </summary>
	public enum DisableCondition
	{
		DisableAfterReverse = -1,
		DoNotDisable = 0,
		DisableAfterForward = 1,
	}
}
