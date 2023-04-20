import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TestService {

  constructor(private httpClient: HttpClient) { }

  postTest(body: any): Observable<any> {
    const headers = new HttpHeaders({
      'Content-Type' : 'application/json',
    })
    console.log(body);

    return this.httpClient.post('http://localhost:8000/test', body)
  }
}

