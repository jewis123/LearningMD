using UnityEngine;
using Unity.MLAgentsExamples;
using Unity.MLAgents;

public class FightArea : Area
{
    public GameObject food;
    public int numFood;
    public bool respawnFood;
    public float range;

    void CreateFood(int num, GameObject type)
    {
        for (int i = 0; i < num; i++)
        {
            GameObject f = Instantiate(type, new Vector3(Random.Range(-range, range), 1f,
                Random.Range(-range, range)) + transform.position,
                Quaternion.Euler(new Vector3(0f, Random.Range(0f, 360f), 90f)));
            f.GetComponent<FoodCreaetLogic>().respawn = respawnFood;
            f.GetComponent<FoodCreaetLogic>().myArea = this;
        }
    }

    public void ResetFoodArea(GameObject[] agents)
    {
        foreach (GameObject agent in agents)
        {
            if (agent.transform.parent == gameObject.transform)
            {
                agent.transform.position = new Vector3(Random.Range(-range, range), 2f,
                    Random.Range(-range, range))
                    + transform.position;
            }
        }

        CreateFood(numFood, food);
    }

    public override void ResetArea()
    {
    }
}
