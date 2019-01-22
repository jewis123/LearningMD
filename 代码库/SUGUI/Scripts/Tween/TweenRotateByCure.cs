using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Transform))]
public class TweenRotateByCure : MonoBehaviour {
	[Header("横坐标为时间，纵坐标为弧度")]
	public AnimationCurve AnimationCurves = new AnimationCurve(new Keyframe(0f, 0f, 0f, 1f), new Keyframe(1f, 1f, 1f, 0f));
	public bool loop;
	public float CallTime;

	private float timer = 0;

	private float MaxTime = 0;

	void OnDisable() {
		timer = 0;
		var Rotation = Quaternion.Euler(new Vector3(0, 0, Mathf.Rad2Deg * 0));
		this.transform.rotation = Rotation;
	}

	void Start() {
		timer = 0;
		MaxTime = AnimationCurves.keys[AnimationCurves.length - 1].time;
	}

	// Update is called once per frame
	void Update() {
		if (timer <= MaxTime) {
			float z = AnimationCurves.Evaluate(timer);
			var Rotation = Quaternion.Euler(new Vector3(0, 0, Mathf.Rad2Deg * z));
			this.transform.rotation = Rotation;
		} else {
			if (loop) {
				timer = 0;
			}
		}
		timer += Time.deltaTime;
	}
}