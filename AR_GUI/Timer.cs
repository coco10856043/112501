using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class Timer : MonoBehaviour
{
    public Text hour;
    public Text minu;
    public Text sec;
    public float secon;
    public int se;
    public int mi;
    public int hr;
    // Start is called before the first frame update
    void OnCollisiion(Collision other)
        { 
            if (other.gameObject.tag == "start")
            {
                this.gameObject.SetActive(false);
                IvokeRepeating("startTime", 1f, 1f);
                CancelIvoke("startTime");
            }
        }
    

    // Update is called once per frame

    void Start()
    {
        
        
    }
    void Update()
    {
        secon += Time.deltaTime;
        Debug.Log(secon);
        if (secon > 0.99999)
        {
            se += 1;
            secon = 0;
        }
        if (se == 60 )
        {
            mi += 1;
            se = 0;
        }
        if (mi == 60)
        {
            hr += 1;
            mi = 0;
        }

        hour.text = hr.ToString();
        minu.text = mi.ToString();
        sec.text = se.ToString();
    }

}
