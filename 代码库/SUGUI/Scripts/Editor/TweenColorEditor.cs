//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(TweenColor))]
public class TweenColorEditor : UITweenerEditor
{
	public override void OnInspectorGUI ()
	{
		GUILayout.Space(6f);
		SUGUIEditorTools.SetLabelWidth(120f);

		TweenColor tw = target as TweenColor;
		GUI.changed = false;

		Color from = EditorGUILayout.ColorField("From", tw.from);
		Color to = EditorGUILayout.ColorField("To", tw.to);

		if (GUI.changed)
		{
            SUGUIEditorTools.RegisterUndo("Tween Change", tw);
			tw.from = from;
			tw.to = to;
            SUGUITools.SetDirty(tw);
		}

		DrawCommonProperties();
	}
}
