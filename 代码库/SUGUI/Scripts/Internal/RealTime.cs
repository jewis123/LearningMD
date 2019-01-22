//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using UnityEngine;

/// <summary>
/// 时间类没有时标-独立的时间。此类修复。
/// </summary>
public class RealTime : MonoBehaviour
{
#if UNITY_4_3
	static RealTime mInst;

	float mRealTime = 0f;
	float mRealDelta = 0f;

	/// <summary>
	/// 实时时间
	/// </summary>

	static public float time
	{
		get
		{
 #if UNITY_EDITOR
			if (!Application.isPlaying) return Time.realtimeSinceStartup;
 #endif
			if (mInst == null) Spawn();
			return mInst.mRealTime;
		}
	}

	/// <summary>
	/// 实时增量时间
	/// </summary>

	static public float deltaTime
	{
		get
		{
 #if UNITY_EDITOR
			if (!Application.isPlaying) return 0f;
 #endif
			if (mInst == null) Spawn();
			return mInst.mRealDelta;
		}
	}

	static void Spawn ()
	{
		GameObject go = new GameObject("_RealTime");
		DontDestroyOnLoad(go);
		mInst = go.AddComponent<RealTime>();
		mInst.mRealTime = Time.realtimeSinceStartup;
	}

	void Update ()
	{
		float rt = Time.realtimeSinceStartup;
		mRealDelta = Mathf.Clamp01(rt - mRealTime);
		mRealTime = rt;
	}
#else
	/// <summary>
	/// 启动实时时间
	/// </summary>
	static public float time { get { return Time.unscaledTime; } }

	/// <summary>
	/// 实时增量时间
	/// </summary>
	static public float deltaTime { get { return Time.unscaledDeltaTime; } }
#endif
}
