using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(TweenLayoutElement))]
public class TweenLayoutElementEditor : UITweenerEditor
{
    public override void OnInspectorGUI()
    {
        GUILayout.Space(6f);
        SUGUIEditorTools.SetLabelWidth(120f);

        TweenLayoutElement tw = target as TweenLayoutElement;
        GUI.changed = false;

        float from = EditorGUILayout.FloatField("From", tw.from);
        float to = EditorGUILayout.FloatField("To", tw.to);

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
