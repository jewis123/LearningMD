using UnityEngine;

public class FoodCreaetLogic : MonoBehaviour
{
    public bool respawn;
    public FightArea myArea;

    public void OnEaten()
    {
        if (respawn)
        {
            GetComponent<Rigidbody>().velocity = Vector3.zero;
            transform.position = new Vector3(Random.Range(-myArea.range, myArea.range),
                3f,
                Random.Range(-myArea.range, myArea.range)) + myArea.transform.position;
        }
        else
        {
            Destroy(gameObject);
        }
    }
}
