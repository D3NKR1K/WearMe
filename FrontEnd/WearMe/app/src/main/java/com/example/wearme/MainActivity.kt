package com.example.wearme

import android.content.Intent
import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_start)

        val linkToSignUp: com.google.android.material.button.MaterialButton = findViewById(R.id.layout_SignUp_button)
        val linkToSignIn: com.google.android.material.button.MaterialButton = findViewById(R.id.layout_SignIn_button)

        linkToSignUp.setOnClickListener {
            try {
                val intent = Intent(this, SignUpActivity::class.java)
                startActivity(intent)
            } catch (e: Exception) {
                Log.e("MainActivity", "Ошибка перехода в SignUpActivity: ${e.message}")
            }
        }

        linkToSignIn.setOnClickListener {
            try {
                val intent = Intent(this, SignInActivity::class.java)
                startActivity(intent)
            } catch (e: Exception) {
                Log.e("MainActivity", "Ошибка перехода в SignInActivity: ${e.message}")
            }
        }
    }
}