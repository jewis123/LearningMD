using UnityEngine;
using System.Collections;
using Unity.MLAgents;
using Unity.MLAgents.Actuators;
using Unity.MLAgents.Sensors;
using System.Collections.Generic;

public class ActivityAgent : Agent
{
    public int score = 0;   //得分
    public GameObject subAgentPrb;
    public Transform fightArea;

    public float biggestSize;
    public float totalSize;
    FightArea fightAreaCom;
    List<SubAgent> m_subAgents = new List<SubAgent>();
    EnvironmentParameters m_ResetParams;
    public FightArea myArea;

    public override void Initialize()
    {
        myArea = FindObjectOfType<FightArea>();
        fightAreaCom = fightArea.GetComponent<FightArea>();
        m_ResetParams = Academy.Instance.EnvironmentParameters;
    }

    public override void OnEpisodeBegin()
    {
        SetResetParameters();
    }

    public void SetResetParameters()
    {
        biggestSize = 1;
        totalSize = 1;
        transform.position += new Vector3(Random.Range(-fightAreaCom.range, fightAreaCom.range), 1f,
                Random.Range(-fightAreaCom.range, fightAreaCom.range)) + myArea.transform.position;
        ClearAllSubAgent();

        GameObject sub = Instantiate<GameObject>(subAgentPrb);
        sub.transform.position = transform.position;
        sub.transform.SetParent(transform);
        SubAgent subAgent = sub.GetComponent<SubAgent>();
        subAgent.OnCreated(1, 2, this);
        m_subAgents.Add(subAgent);
    }

    void ClearAllSubAgent()
    {
        foreach (var item in m_subAgents)
        {
            Destroy(item.gameObject);
        }
        m_subAgents.Clear();
    }

    public override void OnActionReceived(ActionBuffers actionBuffers)
    {
        ActionSegment<int> act = actionBuffers.DiscreteActions;
        var dirToGo = Vector3.zero;

        // var splitCommand = false;
        // var feedCommand = false;
        var forwardAxis = (int)act[0];
        var verticelAxis = (int)act[1];
        // var feedAxis = (int)act[2];
        // var splitAxis = (int)act[3];

        switch (forwardAxis)
        {
            case 1:
                dirToGo = Vector3.back;
                break;
            case 2:
                dirToGo = Vector3.forward;
                break;
        }
        switch (verticelAxis)
        {
            case 1:
                dirToGo = Vector3.left;
                break;
            case 2:
                dirToGo = Vector3.right;
                break;
        }
        // if (splitAxis == 1)
        // {
        //     splitCommand = true;
        // }
        // if (feedAxis == 1)
        // {
        //     feedCommand = true;
        // }

        foreach (var sub in m_subAgents)
        {
            sub.Move(dirToGo);
        }
    }


    /// <summary>
    /// 重写手动操作，并定义离散行为列表
    /// </summary>
    /// <param name="actionsOut"></param>
    public override void Heuristic(in ActionBuffers actionsOut)
    {
        var discreteActionsOut = actionsOut.DiscreteActions;
        discreteActionsOut[0] = 0;   //水平移动,3分量
        discreteActionsOut[1] = 0;   //纵向移动，3分量
        // discreteActionsOut[2] = 0;   //吐食，2分量
        // discreteActionsOut[3] = 0;   //分裂，2分量

        if (Input.GetKey(KeyCode.A))
        {
            discreteActionsOut[0] = 1;
        }
        if (Input.GetKey(KeyCode.D))
        {
            discreteActionsOut[0] = 2;
        }

        if (Input.GetKey(KeyCode.W))
        {
            discreteActionsOut[1] = 1;
        }
        if (Input.GetKey(KeyCode.S))
        {
            discreteActionsOut[1] = 2;
        }

        // discreteActionsOut[2] = Input.GetKey(KeyCode.J) ? 1 : 0;
        // discreteActionsOut[3] = Input.GetKey(KeyCode.K) ? 1 : 0;

    }

    public void LoseChild(SubAgent child)
    {
        if (m_subAgents.Contains(child))
        {
            m_subAgents.Remove(child);
            Destroy(child.gameObject);
        }
        if (m_subAgents.Count == 0)
        {
            EndEpisode();
        }
    }

}
