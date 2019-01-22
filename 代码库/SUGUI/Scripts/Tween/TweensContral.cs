using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TweensContral : MonoBehaviour {

	public List<UITweener> Tweeners = new List<UITweener>();

	private EventDelegate EDOnFinish;
	void Awake() {
		foreach (UITweener tw in Tweeners) {
			tw.enabled = false;
		}
	}

	/// <summary>
	///	播放动画
	/// <param name="fromStart"> fromStart stop not finish Aniam</param>
	/// <param name="forward"> forwrd ? </parma>
	/// <param name= "delay"> delay time </param>
	/// <param name= "realTime"> isRealTime </param>
	/// </summary>
	public void PlayForward(bool fromStart, bool forward = true, float delay = 0, bool realTime = false) {
		if (delay <= 0) {
			playerForward(fromStart);
		} else {
			StartCoroutine(PlayerForward(fromStart, delay, forward, realTime));
		}
	}

	IEnumerator PlayerForward(bool fromStart, float delay, bool forward = true, bool realTime = false) {
		if (realTime) {
			yield return new WaitForSecondsRealtime(delay);
		} else {
			yield return new WaitForSeconds(delay);
		}
		playerForward(fromStart);
	}
	private void playerForward(bool fromStart, bool forward = true) {
		foreach (UITweener uitweener in Tweeners) {
			uitweener.enabled = true;
			if (uitweener.IsInvoking() && !fromStart) { } else {
				if(forward){
					uitweener.ResetToBeginning();
				}
				uitweener.Play(forward);
			}
		}
	}

	private void OnFinish(UITweener uit) {

	}
}