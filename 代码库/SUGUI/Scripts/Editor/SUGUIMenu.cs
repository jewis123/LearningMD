//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEditor;
using System;
using System.Collections.Generic;
using UnityEngine.UI;

/// <summary>
/// 绘制顶级导航菜单
/// </summary>
static public class NGUIMenu
{
#region Tweens

    [MenuItem("XPlugin/UI/SUGUI/Tween/Tween Alpha", false, 8)]
	static void Tween1 () { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenAlpha>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Alpha", true)]
    static bool Tween1a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<MaskableGraphic>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Color", false, 8)]
    static void Tween2() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenColor>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Color", true)]
    static bool Tween2a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<MaskableGraphic>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Width", false, 8)]
    static void Tween3() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenWidth>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Width", true)]
    static bool Tween3a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<RectTransform>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Height", false, 8)]
    static void Tween4() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenHeight>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Height", true)]
    static bool Tween4a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<RectTransform>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Position", false, 8)]
    static void Tween5() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenPosition>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Position", true)]
    static bool Tween5a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Transform>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Rotation", false, 8)]
    static void Tween6() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenRotation>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Rotation", true)]
    static bool Tween6a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Transform>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Scale", false, 8)]
    static void Tween7() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenScale>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Scale", true)]
    static bool Tween7a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Transform>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Transform", false, 8)]
    static void Tween8() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenTransform>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Transform", true)]
    static bool Tween8a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Transform>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Volume", false, 8)]
    static void Tween9() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenVolume>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Volume", true)]
    static bool Tween9a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<AudioSource>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Text", false, 8)]
    static void Tween10() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenText>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Text", true)]
    static bool Tween10a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Text>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Slider", false, 8)]
    static void Tween11() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<TweenSlider>(); }

	[MenuItem("XPlugin/UI/SUGUI/Tween/Tween Slider", true)]
    static bool Tween11a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Slider>() != null); }
#endregion

    #region Interaction


	[MenuItem("XPlugin/UI/SUGUI/Interaction/Button Offset", false, 9)]
    static void Interaction1() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<UIButtonOffset>(); }

	[MenuItem("XPlugin/UI/SUGUI/Interaction/Button Offset", true)]
    static bool Interaction1a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Transform>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Interaction/Button Rotation", false, 9)]
    static void Interaction2() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<UIButtonRotation>(); }

	[MenuItem("XPlugin/UI/SUGUI/Interaction/Button Rotation", true)]
    static bool Interaction2a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Transform>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Interaction/Button Scale", false, 9)]
    static void Interaction3() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<UIButtonScale>(); }

	[MenuItem("XPlugin/UI/SUGUI/Interaction/Button Scale", true)]
    static bool Interaction3a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Transform>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Interaction/Button Activate", false, 9)]
    static void Interaction4() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<UIButtonActivate>(); }

	[MenuItem("XPlugin/UI/SUGUI/Interaction/Button Activate", true)]
    static bool Interaction4a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Transform>() != null); }

	[MenuItem("XPlugin/UI/SUGUI/Interaction/Slider Colors", false, 9)]
    static void Interaction5() { if (Selection.activeGameObject != null) Selection.activeGameObject.AddMissingComponent<SliderColors>(); }

	[MenuItem("XPlugin/UI/SUGUI/Interaction/Slider Colors", true)]
    static bool Interaction5a() { return (Selection.activeGameObject != null) && (Selection.activeGameObject.GetComponent<Slider>() != null); }
    #endregion

	[MenuItem("XPlugin/UI/SUGUI/Help", false, 12)]
    static public void Help() { ShowHelp(); }

    /// <summary>
    /// 显示帮助
    /// </summary>
    static public void ShowHelp()
    {
        Application.OpenURL("http://www.xiaobao1993.com");
    }
}
