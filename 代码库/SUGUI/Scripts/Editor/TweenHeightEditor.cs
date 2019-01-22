//----------------------------------------------
//            NGUI: Next-Gen UI kit
// Copyright © 2011-2014 Tasharen Entertainment
//----------------------------------------------

using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(TweenHeight))]
public class TweenHeightEditor : UITweenerEditor
{
	public override void OnInspectorGUI ()
	{
		GUILayout.Space(6f);
        SUGUIEditorTools.SetLabelWidth(120f);

		TweenHeight tw = target as TweenHeight;
		GUI.changed = false;

		int from = EditorGUILayout.IntField("From", tw.from);
		int to = EditorGUILayout.IntField("To", tw.to);
		bool table = EditorGUILayout.Toggle("Update Table", tw.updateTable);

		if (from < 0) from = 0;
		if (to < 0) to = 0;

		if (GUI.changed)
		{
            SUGUIEditorTools.RegisterUndo("Tween Change", tw);
			tw.from = from;
			tw.to = to;
			tw.updateTable = table;
			SUGUITools.SetDirty(tw);
		}

		DrawCommonProperties();
	}
}
