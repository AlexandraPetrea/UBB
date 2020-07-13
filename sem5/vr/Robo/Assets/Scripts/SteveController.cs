using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public enum CharacterState
{
    idle,
    walking, 
    running, 
    jumping,
    dancing,
}

[RequireComponent(typeof(Rigidbody))]
public class SteveController : MonoBehaviour {

    public MemberController left_arm; 
    public MemberController left_forearm; 
    public MemberController right_arm; 
    public MemberController right_forearm; 
    public MemberController left_leg; 
    public MemberController left_lower_leg; 
    public MemberController right_leg;
    public MemberController right_lower_leg;

    public CharacterState _state;
    public float normalSpeed = 10.0f;
    public float runningSpeed = 20.0f; 

    public float rotationSpeed = 100.0f;

    public float membersNormalSpeed = 200.0f; 
    public float membersRunningSpeed = 300.0f;

    public Vector3 jumpForward = new Vector3(0.0f, 2.0f, 0.0f);
    public float jumpForce = 2.0f; 
    public bool isGrounded;
    Rigidbody rigidbody;

    // Use this for initialization
    void Start () {
        rigidbody = GetComponent<Rigidbody>();
        _state = CharacterState.idle;
    }
	
	// Update is called once per frame
	void Update () {

       _state = GetState();

        if (_state == CharacterState.dancing)
            this.Move(this.normalSpeed, this.membersNormalSpeed);

        if (_state == CharacterState.walking)
            this.Move(this.normalSpeed, this.membersNormalSpeed);

        if (_state == CharacterState.running)
            this.Move(this.runningSpeed, this.membersRunningSpeed); 

        if (_state == CharacterState.jumping)
            this.Jump();
       
        if (_state == CharacterState.idle)
            this.ReturnToIdle(this.membersRunningSpeed);

        this.Spin();
    }

    CharacterState GetState()
    {
        
        if (Input.GetButton("Jump") )
            //&& this.isGrounded)
        {
            return CharacterState.dancing;
        }

        if (Input.GetButton("Vertical"))
        {
            if (Input.GetButton("Sprint"))
            {
               return CharacterState.running; 
            }
           
            return CharacterState.walking;
            
        }

        return CharacterState.idle;
    }

    void Spin()
    {
        float rotation = Input.GetAxis("Horizontal") * this.rotationSpeed * Time.deltaTime;
        transform.Rotate(0, rotation, 0);
    }

    void MoveVertical(float playerSpeed)
    {
        float translation = Input.GetAxis("Vertical") * playerSpeed * Time.deltaTime;
        transform.Translate(0, 0, translation);
    }

    void Move(float playerSpeed, float membersSpeed)
    {
        this.MoveMembers(membersSpeed);
        this.MoveVertical(playerSpeed);
    }

    private void MoveMembers(float speed)
    {
        this.left_arm.Move(speed);
        this.left_forearm.Move(speed / 2);
        this.right_arm.Move(speed);
        this.right_forearm.Move(speed / 2);
        this.left_leg.Move(speed);
        this.left_lower_leg.Move(speed / 2);
        this.right_leg.Move(speed);
        this.right_lower_leg.Move(speed / 2); 

    }

    private void ReturnToIdle(float speed)
    {
        this.left_arm.ReturnToIdle(speed);
        this.left_forearm.ReturnToIdle(50/100 * speed); 
        this.right_arm.ReturnToIdle(speed);
        this.right_forearm.ReturnToIdle(50/100 * speed); 
        this.left_leg.ReturnToIdle(speed);
        this.left_lower_leg.ReturnToIdle(80/100 * speed);
        this.right_leg.ReturnToIdle(speed);
        this.right_lower_leg.ReturnToIdle(80/100 * speed); 
    }
    private void Jump()
    {
        rigidbody.AddForce(this.jumpForward * this.jumpForce, ForceMode.Impulse);
    }

    void OnCollisionEnter(Collision other)
    { 
        if (other.gameObject.tag == "Surface")
        {
            isGrounded = true;
        }
    }

    void OnCollisionExit(Collision other)
    {

        if (other.gameObject.tag == "Surface")
        {
            isGrounded = false;
        }
    }
  

}
