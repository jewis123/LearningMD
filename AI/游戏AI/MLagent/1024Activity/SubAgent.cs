using UnityEngine;
using Unity.MLAgentsExamples;

public class SubAgent : MonoBehaviour
{
    public float childSize;
    public float childSpeed;

    public ActivityAgent parent;
    private GroundContact contact;
    FightManager manager;
    private FightArea area;

    Rigidbody rigid;

    void OnEnable()
    {
        rigid = GetComponent<Rigidbody>();
        contact = GetComponent<GroundContact>();
        area = FindObjectOfType<FightArea>();
        manager = FindObjectOfType<FightManager>();
    }

    public void OnCreated(int size, int speed, ActivityAgent parent)
    {
        childSize = size;
        childSpeed = speed;
        this.parent = parent;
    }

    public void Move(Vector3 dir)
    {
        if (!contact.touchingGround)
        {
            return;
        }

        if (transform.position.y < -2)
        {
            parent.AddReward(-1);
            parent.EndEpisode();
        }

        rigid.AddForce(dir * childSpeed, ForceMode.VelocityChange);
        if (rigid.velocity.sqrMagnitude > 25f) // slow it down
        {
            rigid.velocity *= 0.95f;
        }
    }

    void OnCollisionEnter(Collision collision)
    {
        GameObject hitObj = collision.gameObject;
        SubAgent hitAgent = hitObj.GetComponent<SubAgent>();
        if (hitObj.CompareTag("food"))
        {
            parent.AddReward(0.3f);
            hitObj.GetComponent<FoodCreaetLogic>().OnEaten();
        }

        if (hitObj.CompareTag("wall"))
        {
            parent.AddReward(-0.5f);
            parent.LoseChild(this);
        }

        if (hitObj.CompareTag("agent"))
        {
            if (hitAgent.parent != parent)
            {
                if (childSize < hitAgent.childSize)
                {
                    OnEaten(true);
                }
                else if (childSize > hitAgent.childSize)
                {
                    parent.AddReward(1);
                    Grow(hitAgent.childSize);
                }
            }
            else
            {
                if (childSize > hitAgent.childSize)
                {
                    hitAgent.OnEaten(false);
                    Grow(hitAgent.childSize);
                }
            }
        }
    }

    public void OnEaten(bool isEnermyEat)
    {
        if (isEnermyEat)
        {
            parent.AddReward(-1);
        }
        parent.LoseChild(this);
    }

    private void Grow(float size)
    {
        childSize = childSize + size;
        childSpeed = Mathf.Min(0.01f, childSpeed - childSize / 30);
        if (childSize > parent.biggestSize)
        {
            parent.biggestSize = childSize;
        }
        parent.totalSize += size;
        if (area.numFood == 0)
        {
            parent.EndEpisode();
        }
    }

}
