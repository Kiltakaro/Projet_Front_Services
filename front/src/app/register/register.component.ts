import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { RegisterService } from '../services/register.service';

@Component({
  selector: 'app-register',
  imports: [ReactiveFormsModule],
  standalone: true,
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  registerForm: FormGroup;

  constructor(private fb: FormBuilder, private registerService: RegisterService) {
    this.registerForm = this.fb.group({
      username: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  onSubmit() {
    console.log('Formulaire soumis'); // Log pour vérifier que la méthode est appelée
    console.log('Données du formulaire:', this.registerForm.value); // Log des données envoyées
  
    if (this.registerForm.valid) {
      this.registerService.registerUser(this.registerForm.value).subscribe({
        next: (response) => {
          console.log('Réponse du serveur:', response); // Log de la réponse API
          alert('Inscription réussie');
        },
        error: (error) => {
          console.error('Erreur de l\'API:', error); // Log des erreurs API
          alert('Erreur lors de l\'inscription');
        },
      });
    } else {
      console.warn('Formulaire invalide');
    }
  }
  
}
