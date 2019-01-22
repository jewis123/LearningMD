using UnityEngine;
using System.Collections;
using UnityEngine.UI;


public class TweenCanvasGroupAlpha : UITweener {
    [Range(0f, 1f)]
    public float from = 1f;
    [Range(0f, 1f)]
    public float to = 1f;

    CanvasGroup mCanvasGroup;

    public CanvasGroup CachedCanvasGroup
    {
        get
        {
            if (mCanvasGroup == null)
            {
                mCanvasGroup = GetComponent<CanvasGroup>();
                if (mCanvasGroup == null) mCanvasGroup = GetComponentInChildren<CanvasGroup>();
                if (mCanvasGroup == null) mCanvasGroup = gameObject.AddComponent<CanvasGroup>();
            }
            return mCanvasGroup;
        }
    }

    public float value
    {
        get
        {
            return alpha;
        }
        set
        {
            alpha = value;
        }
    }

    public float alpha
    {
        get { return CachedCanvasGroup.alpha; }
        set { CachedCanvasGroup.alpha = value; }
    }
    protected override void OnUpdate(float factor, bool isFinished) { value = Mathf.Lerp(from, to, factor); }

    /// <summary>
    /// 开始补间操作
    /// </summary>

    static public TweenCanvasGroupAlpha Begin(GameObject go, float duration, float alpha)
    {
        TweenCanvasGroupAlpha comp = UITweener.Begin<TweenCanvasGroupAlpha>(go, duration);
        comp.from = comp.value;
        comp.to = alpha;

        if (duration <= 0f)
        {
            comp.Sample(1f, true);
            comp.enabled = false;
        }
        return comp;
    }

    public override void SetStartToCurrentValue() { from = value; }
    public override void SetEndToCurrentValue() { to = value; }
}
