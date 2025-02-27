package com.example.wearme

import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import com.example.wearme.databinding.ActivityStartBinding
import com.google.android.material.color.DynamicColors

class MainActivity : AppCompatActivity() {
  private lateinit var binding: ActivityStartBinding

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
      DynamicColors.applyToActivitiesIfAvailable(application)
    }

    binding = ActivityStartBinding.inflate(layoutInflater)
    setContentView(binding.root)

    setupNavigation()
  }

  private fun setupNavigation() {
    binding.layoutSignUpButton.setOnClickListener {
      navigateTo(SignUpActivity::class.java)
    }

    binding.layoutSignInButton.setOnClickListener {
      navigateTo(SignInActivity::class.java)
    }
  }

  private fun navigateTo(activityClass: Class<*>) {
    try {
      startActivity(Intent(this, activityClass))

    } catch (e: Exception) {
      handleNavigationError(e, activityClass.simpleName)
    }
  }

  private fun handleNavigationError(e: Exception, activityName: String) {
    Log.e("MainActivity", "Error navigating to $activityName: ${e.message}")
  }
}