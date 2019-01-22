//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(TweenAlpha))]
public class TweenAlphaEditor : UITweenerEditor
{
    
	public override void OnInspectorGUI ()
	{
		GUILayout.Space(6f); 
        SUGUIEditorTools.SetLabelWidth(120f);

		TweenAlpha tw = target as TweenAlpha;
		GUI.changed = false;

		float from = EditorGUILayout.Slider("From", tw.from, 0f, 1f);
		float to = EditorGUILayout.Slider("To", tw.to, 0f, 1f);

		if (GUI.changed)
		{
            SUGUIEditorTools.RegisterUndo("Tween Change", tw);
			tw.from = from;
			tw.to = to;
            UnityEditor.EditorUtility.SetDirty(tw);
		}

		DrawCommonProperties();
	}

}
