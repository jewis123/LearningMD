//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEditor;
using UnityEngine;
using System.Collections.Generic;
using System.Reflection;

/// <summary>
/// 界面绘制工具类
/// </summary>
#if UNITY_3_5
[CustomEditor(typeof(UITweener))]
#else
[CustomEditor(typeof(UITweener), true)]
#endif
public class SUGUIEditorTools : Editor 
{

    /// <summary>
    /// 设置标签宽
    /// </summary>
    static public void SetLabelWidth(float width)
    {
        EditorGUIUtility.labelWidth = width;
    }

    /// <summary>
    /// 绘制一个标题标签
    /// </summary>

    static public bool DrawHeader(string text) { return DrawHeader(text, text, false); }

    /// <summary>
    /// 绘制一个标题标签
    /// </summary>

    static public bool DrawHeader(string text, string key) { return DrawHeader(text, key, false); }

    /// <summary>
    /// 绘制一个标题标签
    /// </summary>

    static public bool DrawHeader(string text, bool detailed) { return DrawHeader(text, text, detailed); }

    /// <summary>
    /// 绘制一个标题标签
    /// </summary>

    static public bool DrawHeader(string text, string key, bool forceOn)
    {
        bool state = EditorPrefs.GetBool(key, true);

        
        if (!forceOn && !state) GUI.backgroundColor = new Color(0.8f, 0.8f, 0.8f);
        GUILayout.BeginHorizontal();
        GUI.changed = false;

        text = "<b><size=11>" + text + "</size></b>";
        if (state) text = "\u25BC " + text;
        else text = "\u25BA " + text;
        if (!GUILayout.Toggle(true, text, "dragtab", GUILayout.MinWidth(20f))) state = !state;
       
        if (GUI.changed) EditorPrefs.SetBool(key, state);

        GUILayout.EndHorizontal();
        GUI.backgroundColor = Color.white;
        if (!forceOn && !state) GUILayout.Space(3f);
        return state;
    }


    /// <summary>
    /// 开始绘制内容区域
    /// </summary>
    static public void BeginContents()
    {
        GUILayout.BeginHorizontal();
        EditorGUILayout.BeginHorizontal("AS TextArea", GUILayout.MinHeight(10f));
        GUILayout.BeginVertical();
        GUILayout.Space(2f);
    }
    /// <summary>
    /// 结束界面绘制
    /// </summary>

    static public void EndContents()
    {
        GUILayout.Space(3f);
        GUILayout.EndVertical();
        EditorGUILayout.EndHorizontal();

        GUILayout.Space(3f);
        GUILayout.EndHorizontal();
        GUILayout.Space(3f);
    }


    /// <summary>
    /// 绘制委托事件
    /// </summary>

    static public void DrawEvents(string text, Object undoObject, List<EventDelegate> list)
    {
        DrawEvents(text, undoObject, list, null, null);
    }

    /// <summary>
    /// 绘制委托事件
    /// </summary>

    static public void DrawEvents(string text, Object undoObject, List<EventDelegate> list, string noTarget, string notValid)
    {
        if (!SUGUIEditorTools.DrawHeader(text, text, false)) return;

        
        SUGUIEditorTools.BeginContents();
        GUILayout.BeginHorizontal();
        GUILayout.BeginVertical();

        EventDelegateEditor.Field(undoObject, list, notValid, notValid);

        GUILayout.EndVertical();
        GUILayout.EndHorizontal();
        SUGUIEditorTools.EndContents();
    }

    /// <summary>
    /// 创建指定对象撤消点
    /// </summary>
    static public void RegisterUndo(string name, params Object[] objects)
    {
        if (objects != null && objects.Length > 0)
        {
            UnityEditor.Undo.RecordObjects(objects, name);

            foreach (Object obj in objects)
            {
                if (obj == null) continue;
                EditorUtility.SetDirty(obj);
            }
        }
    }

    /// <summary>
    /// 在右侧绘制 18 像素 用于字段对齐
    /// </summary>

    static public void DrawPadding()
    {
        GUILayout.Space(18f);
    }
}
