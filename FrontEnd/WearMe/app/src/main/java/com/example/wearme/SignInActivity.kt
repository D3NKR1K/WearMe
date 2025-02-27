package com.example.wearme

import android.content.Intent
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Patterns
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.example.wearme.databinding.ActivityLogBinding

class SignInActivity : AppCompatActivity() {
  private lateinit var binding: ActivityLogBinding

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    binding = ActivityLogBinding.inflate(layoutInflater)
    setContentView(binding.root)

    binding.linkToSignUp.setOnClickListener {
      startActivity(Intent(this, SignUpActivity::class.java))
    }

    setupValidation()
  }

  private fun setupValidation() {
    listOf(
      binding.inputUserEmail to ::validateEmail,
    ).forEach { (field, validator) ->
      field.addTextChangedListener(object : TextWatcher {
        override fun afterTextChanged(s: Editable?) { validator() }
        override fun beforeTextChanged(s: CharSequence?, p1: Int, p2: Int, p3: Int) {}
        override fun onTextChanged(s: CharSequence?, p1: Int, p2: Int, p3: Int) {}
      })
    }
  }

  // userEmail validation
  private fun validateEmail(): Boolean {
    val email = binding.inputUserEmail.text.toString().trim()
    return when {
      email.isEmpty() -> showError(binding.layoutSignInEmail, getString(R.string.error_empty_email))
      !Patterns.EMAIL_ADDRESS.matcher(email).matches() -> showError(binding.layoutSignInEmail, getString(R.string.error_invalid_email))
      else -> clearError(binding.layoutSignInEmail)
    }
  }

  private fun showError(layout: com.google.android.material.textfield.TextInputLayout, message: String): Boolean {
    layout.error = message
    layout.boxStrokeColor = ContextCompat.getColor(this, R.color.red)
    return false
  }

  private fun clearError(layout: com.google.android.material.textfield.TextInputLayout): Boolean {
    layout.error = null
    layout.boxStrokeColor = ContextCompat.getColor(this, R.color.black)
    return true
  }
}