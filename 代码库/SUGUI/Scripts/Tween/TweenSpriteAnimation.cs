//----------------------------------------------
//			        SUGUI
// Copyright © 2012-2015 xiaobao1993.com
//----------------------------------------------

using System;
using System.Collections;
using System.Collections.Generic;
#if UNITY_EDITOR
using UnityEditor;
#endif
using UnityEngine;
using UnityEngine.UI;

[RequireComponent(typeof(Image))]
public class TweenSpriteAnimation : MonoBehaviour {
	private Image ImageSource;
	private int currFrame = 0;
	private float timer = 0;

	public float FPS = 5;

	[SerializeField] [Header("放入序列帧")]
	private Texture2D texFrame;

	[HeavyDutyInspector.Button("引用序列帧","ApplyTexture",true)]
	public bool isApplyTexture;
	
	public List<Sprite> SpriteFrames;
	public bool IsPlaying = false;
	public bool Forward = true;
	public bool AutoPlay = false;
	public bool Loop = false;
	public bool PingPong = false;

	public int FrameCount {
		get {
			return SpriteFrames.Count;
		}
	}

	void Awake() {
		ImageSource = GetComponent<Image>();
	}

	void Start() {
		if (AutoPlay) {
			Play();
		} else {
			IsPlaying = false;
		}

	}

	private void SetSprite(int idx) {
		ImageSource.sprite = SpriteFrames[idx];
		//该部分为设置成原始图片大小，如果只需要显示Image设定好的图片大小，注释掉该行即可。
		//ImageSource.SetNativeSize ();
	}

	public void Play() {
		IsPlaying = true;
		Forward = true;
	}

	private void Update() {
		if (!IsPlaying || 0 == FrameCount) {
			return;
		}
		timer += Time.deltaTime;
		if (timer > 1 / FPS) {
			timer = 0;

			if (Forward) {
				currFrame++;
			} else {
				currFrame--;
			}

			if (currFrame >= FrameCount) {
				if (Loop) {
					currFrame = 0;
				} else if (PingPong) {
					Forward = false;
					currFrame = FrameCount - 2;
				} else {
					IsPlaying = false;
					return;
				}
			}
			if (currFrame < 0) {
				if (Loop) {
					currFrame = FrameCount - 1;
				} else if (PingPong) {
					Forward = true;
					currFrame += 2;
				} else {
					IsPlaying = false;
					return;
				}
			}

			SetSprite(currFrame);
		}
	}

	public void SetFrames(List<Sprite> sprites){
		SpriteFrames = sprites;
	}
	
#if UNITY_EDITOR
	[ContextMenu("ApplyTexture")]
	void ApplyTexture() {
			if(texFrame==null){
				Debug.LogError("NULL texFrema");
			}
			string path  = AssetDatabase.GetAssetPath(texFrame);
			TextureImporter imp = AssetImporter.GetAtPath(path) as TextureImporter;
			if(imp.textureType!= TextureImporterType.Sprite){
				Debug.LogError("ERROR TextureImporterType");
			}
			if(imp.spriteImportMode!=SpriteImportMode.Multiple){
				Debug.LogError("Not Mutiple Sprite");
			}
			SpriteFrames.Clear();
			foreach(var data in AssetDatabase.LoadAllAssetRepresentationsAtPath(path)){
				SpriteFrames.Add(data as Sprite);
			}
		
	}
#endif

}