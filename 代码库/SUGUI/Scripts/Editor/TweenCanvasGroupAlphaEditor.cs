using UnityEditor;
using UnityEngine;
using System.Collections;
[CustomEditor(typeof(TweenCanvasGroupAlpha))]
public class TweenCanvasGroupAlphaEditor : UITweenerEditor {

    public override void OnInspectorGUI()
    {
        GUILayout.Space(6f);
        SUGUIEditorTools.SetLabelWidth(120f);

        TweenCanvasGroupAlpha tw = target as TweenCanvasGroupAlpha;
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
