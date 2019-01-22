//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------
using UnityEngine;
using System.Collections;

public static class SUGUITools  
{

    /// <summary>
    ///  Class + Function 转换为 Class.Function.
    /// </summary>
    static public string GetFuncName(object obj, string method)
    {
        if (obj == null) return "<null>";
        string type = obj.GetType().ToString();
        int period = type.LastIndexOf('/');
        if (period > 0) type = type.Substring(period + 1);
        return string.IsNullOrEmpty(method) ? type : type + "/" + method;
    }

    /// <summary>
    /// 添加缺少的组件
    /// </summary>
    static public T AddMissingComponent<T>(this GameObject go) where T : Component
    {
#if UNITY_FLASH
		object comp = go.GetComponent<T>();
#else
        T comp = go.GetComponent<T>();
#endif
        if (comp == null)
        {
#if UNITY_EDITOR
            if (!Application.isPlaying)
                RegisterUndo(go, "Add " + typeof(T));
#endif
            comp = go.AddComponent<T>();
        }
#if UNITY_FLASH
		return (T)comp;
#else
        return comp;
#endif
    }

    static public void RegisterUndo(UnityEngine.Object obj, string name)
    {
#if UNITY_EDITOR
        UnityEditor.Undo.RecordObject(obj, name);
        UnityEditor.EditorUtility.SetDirty(obj);
#endif
    }

    static public void SetDirty(Object obj)
    {
        #if UNITY_EDITOR
        UnityEditor.EditorUtility.SetDirty(obj);
#endif
    }


    public static string RemoveSpaceInString(string ori)
    {
        string final = ori.Replace(" ","");
        return final;
    }





}
