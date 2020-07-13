import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Discipline} from "./discipline.model";

@Injectable()
export class DisciplineService {
  private disciplinesUrl = 'http://localhost:8080/api/disciplines';

  constructor(private httpClient: HttpClient) {
  }

  getDisciplines(): Observable<Discipline[]> {
    return this.httpClient
      .get<Array<Discipline>>(this.disciplinesUrl);
  }

  getDiscipline(id: number): Observable<Discipline> {
    return this.getDisciplines()
      .map(disciplines => disciplines.find(discipline => discipline.id === id));
  }
}
