using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MemberController : MonoBehaviour {

    public GameObject joint;
    public bool inverse;
    public float max_angle = 90.0f;
    public float min_angle = -90.0f; 

    private float angle = 0.0f; 
    private int modifier = 1;
    private float idle_min = -2.0f; 
    private float idle_max = 2.0f; 

	// Use this for initialization
	void Start () {
		if (inverse)
        {
            modifier = -1; 
        }
	}
	
    public void Move (float speed)
    {
        
        // Spin the member around the shoulder origin at <speed> degrees/second.
        transform.RotateAround(joint.transform.position, modifier * joint.transform.right, speed * Time.deltaTime);

        angle +=  modifier * speed * Time.deltaTime;

        if (angle <= min_angle)
        {
            modifier *= -1;
            angle = min_angle; 
        }

        if (angle >= max_angle)
        {
            modifier *= -1;
            angle = max_angle; 
        }
        
    }

    public void ReturnToIdle(float speed)
    {
        if (idle_min <= angle && angle <= idle_max)
            return;

        if (angle < 0)
        {
            modifier = 1; 

        }else if (angle > 0)
        {
            modifier = -1; 
        }

        transform.RotateAround(joint.transform.position, modifier * joint.transform.right, speed * Time.deltaTime);

        angle += modifier * speed * Time.deltaTime;
    
    }
}
