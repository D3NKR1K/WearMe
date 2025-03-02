package com.example.wearme

import android.content.Intent
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Patterns
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.example.wearme.databinding.ActivityRegBinding

class SignUpActivity : AppCompatActivity() {
  private lateinit var binding : ActivityRegBinding

  override fun onCreate(savedInstanceState : Bundle?) {
    super.onCreate(savedInstanceState)
    binding = ActivityRegBinding.inflate(layoutInflater)
    setContentView(binding.root)

    binding.linkToSignIn.setOnClickListener {
      startActivity(Intent(this, SignInActivity::class.java))
    }

    setupValidation()

    binding.layoutSignUpButton.setOnClickListener {
      if (isValidInput()) {
        // start to register user
      } else {
        // incorrect user data
      }
    }

  }

  private fun isValidInput() : Boolean {
    return validateName() && validateEmail() && validatePassword();
  }

  private fun setupValidation() {
    listOf(
      binding.inputUserName to ::validateName,
      binding.inputUserEmail to ::validateEmail,
      binding.inputUserPassword to ::validatePassword
    ).forEach { (field, validator) ->
      field.addTextChangedListener(object : TextWatcher {
        override fun afterTextChanged(s : Editable?) {
          validator()
        }

        override fun beforeTextChanged(s : CharSequence?, p1 : Int, p2 : Int, p3 : Int) {}
        override fun onTextChanged(s : CharSequence?, p1 : Int, p2 : Int, p3 : Int) {}
      })
    }
  }

  // userName validation
  private fun validateName() : Boolean {
    val name = binding.inputUserName.text.toString().trim()
    return when {
      name.isEmpty() -> showError(binding.layoutSignUpName, getString(R.string.error_empty_name))
      name.length < 3 -> showError(binding.layoutSignUpName, getString(R.string.error_short_name))
      else -> clearError(binding.layoutSignUpName)
    }
  }

  // userEmail validation
  private fun validateEmail() : Boolean {
    val email = binding.inputUserEmail.text.toString().trim()
    return when {
      email.isEmpty() -> showError(binding.layoutSignUpEmail, getString(R.string.error_empty_email))
      !Patterns.EMAIL_ADDRESS.matcher(email).matches() -> showError(
        binding.layoutSignUpEmail,
        getString(R.string.error_invalid_email)
      )

      else -> clearError(binding.layoutSignUpEmail)
    }
  }

  // userPassword validation
  private fun validatePassword() : Boolean {
    val password = binding.inputUserPassword.text.toString().trim()
    return when {
      password.isEmpty() -> showError(
        binding.layoutSignUpPassword,
        getString(R.string.error_empty_password)
      )

      password.length < 8 -> showError(
        binding.layoutSignUpPassword,
        getString(R.string.error_short_password)
      )

      !password.contains(Regex("[A-Z]")) -> showError(
        binding.layoutSignUpPassword,
        getString(R.string.error_no_uppercase)
      )

      else -> clearError(binding.layoutSignUpPassword)
    }
  }

  private fun showError(
    layout : com.google.android.material.textfield.TextInputLayout,
    message : String
  ) : Boolean {
    layout.error = message
    layout.boxStrokeColor = ContextCompat.getColor(this, R.color.red)
    return false
  }

  private fun clearError(layout : com.google.android.material.textfield.TextInputLayout) : Boolean {
    layout.error = null
    layout.boxStrokeColor = ContextCompat.getColor(this, R.color.black)
    return true
  }
}