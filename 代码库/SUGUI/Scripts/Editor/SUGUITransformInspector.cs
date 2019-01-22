//----------------------------------------------
//			 SUGUI: Transform值一键复位
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;
using UnityEditor;

[CanEditMultipleObjects]
[CustomEditor(typeof(Transform), true)]
public class SUGUITransformInspector : Editor
{
    static public SUGUITransformInspector instance;

	SerializedProperty mPos;
	SerializedProperty mRot;
	SerializedProperty mScale;

	void OnEnable ()
	{
		instance = this;
		mPos = serializedObject.FindProperty("m_LocalPosition");
		mRot = serializedObject.FindProperty("m_LocalRotation");
		mScale = serializedObject.FindProperty("m_LocalScale");
	}

	void OnDestroy () { instance = null; }

	/// <summary>
	/// 开始绘制Transform
	/// </summary>
	public override void OnInspectorGUI ()
	{
        EditorGUIUtility.labelWidth = 15;
        
		serializedObject.Update();
		DrawPosition();
		DrawRotation();
		DrawScale();

        serializedObject.ApplyModifiedProperties();
	}

    /// <summary>
    /// 绘制坐标
    /// </summary>
	void DrawPosition ()
	{
		GUILayout.BeginHorizontal();
		{
			bool reset = GUILayout.Button("P", GUILayout.Width(20f));

			EditorGUILayout.PropertyField(mPos.FindPropertyRelative("x"));
			EditorGUILayout.PropertyField(mPos.FindPropertyRelative("y"));
			EditorGUILayout.PropertyField(mPos.FindPropertyRelative("z"));

			if (reset) mPos.vector3Value = Vector3.zero;
		}
		GUILayout.EndHorizontal();
	}

    /// <summary>
    /// 绘制形变
    /// </summary>
	void DrawScale ()
	{
		GUILayout.BeginHorizontal();
		{
			bool reset = GUILayout.Button("S", GUILayout.Width(20f));

			EditorGUILayout.PropertyField(mScale.FindPropertyRelative("x"));
			EditorGUILayout.PropertyField(mScale.FindPropertyRelative("y"));
			EditorGUILayout.PropertyField(mScale.FindPropertyRelative("z"));

			if (reset) mScale.vector3Value = Vector3.one;
		}
		GUILayout.EndHorizontal();
	}

    #region 旋转个坑爹玩意......因为四元属性绘制没有原生支持
    enum Axes : int
	{
		None = 0,
		X = 1,
		Y = 2,
		Z = 4,
		All = 7,
	}

	Axes CheckDifference (Transform t, Vector3 original)
	{
		Vector3 next = t.localEulerAngles;

		Axes axes = Axes.None;

        if (Differs(next.x, original.x)) axes |= Axes.X;
		if (Differs(next.y, original.y)) axes |= Axes.Y;
		if (Differs(next.z, original.z)) axes |= Axes.Z;

		return axes;
	}

	Axes CheckDifference (SerializedProperty property)
	{
		Axes axes = Axes.None;

		if (property.hasMultipleDifferentValues)
		{
			Vector3 original = property.quaternionValue.eulerAngles;

			foreach (Object obj in serializedObject.targetObjects)
			{
				axes |= CheckDifference(obj as Transform, original);
				if (axes == Axes.All) break;
			}
		}
		return axes;
	}

	/// <summary>
	/// 绘制一个可编辑的浮动区域
	/// </summary>
	/// <param name="hidden">是否值用 -- 代替</param>
	static bool FloatField (string name, ref float value, bool hidden, GUILayoutOption opt)
	{
		float newValue = value;
		GUI.changed = false;

		if (!hidden)
		{
            newValue = EditorGUILayout.FloatField(name, newValue, opt);
		}
		else
		{
			float.TryParse(EditorGUILayout.TextField(name, "--", opt), out newValue);
		}

		if (GUI.changed && Differs(newValue, value))
		{
			value = newValue;
			return true;
		}
		return false;
	}

	/// <summary>
	/// 由于 Mathf.Approximately 太敏感.
	/// </summary>

	static bool Differs (float a, float b) { return Mathf.Abs(a - b) > 0.0001f; }

    /// <summary>
    /// 绘制旋转
    /// </summary>
	void DrawRotation ()
	{
		GUILayout.BeginHorizontal();
		{
			bool reset = GUILayout.Button("R", GUILayout.Width(20f));

			Vector3 visible = (serializedObject.targetObject as Transform).localEulerAngles;

			visible.x = WrapAngle(visible.x);
			visible.y = WrapAngle(visible.y);
			visible.z = WrapAngle(visible.z);

			Axes changed = CheckDifference(mRot);
			Axes altered = Axes.None;

			GUILayoutOption opt = GUILayout.MinWidth(30f);

			if (FloatField("X", ref visible.x, (changed & Axes.X) != 0, opt)) altered |= Axes.X;
			if (FloatField("Y", ref visible.y, (changed & Axes.Y) != 0, opt)) altered |= Axes.Y;
			if (FloatField("Z", ref visible.z, (changed & Axes.Z) != 0, opt)) altered |= Axes.Z;

			if (reset)
			{
				mRot.quaternionValue = Quaternion.identity;
			}
			else if (altered != Axes.None)
			{
				RegisterUndo("Change Rotation", serializedObject.targetObjects);

				foreach (Object obj in serializedObject.targetObjects)
				{
					Transform t = obj as Transform;
					Vector3 v = t.localEulerAngles;

					if ((altered & Axes.X) != 0) v.x = visible.x;
					if ((altered & Axes.Y) != 0) v.y = visible.y;
					if ((altered & Axes.Z) != 0) v.z = visible.z;

					t.localEulerAngles = v;
				}
			}
		}
		GUILayout.EndHorizontal();
	}

    /// <summary>
    /// 保证角在 180到-180度之间
    /// </summary>

    [System.Diagnostics.DebuggerHidden]
    [System.Diagnostics.DebuggerStepThrough]
    static public float WrapAngle(float angle)
    {
        while (angle > 180f) angle -= 360f;
        while (angle < -180f) angle += 360f;
        return angle;
    }


    /// <summary>
    /// 创建制定对象的撤消点
    /// </summary>
    static public void RegisterUndo(string name, params Object[] objects)
    {
        if (objects != null && objects.Length > 0)
        {
            UnityEditor.Undo.RecordObjects(objects, name);

            foreach (Object obj in objects)
            {
                if (obj == null) continue;
                SUGUITools.SetDirty(obj);
            }
        }
    }
    #endregion

}
