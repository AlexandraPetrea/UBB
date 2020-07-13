import {Component, OnInit} from "@angular/core";
import {Discipline} from "../shared/discipline.model";
import {DisciplineService} from "../shared/discipline.service";


@Component({
  moduleId: module.id,
  selector: 'ubb-discipline-list',
  templateUrl: './discipline-list.component.html',
  styleUrls: ['./discipline-list.component.css'],
})
export class DisciplineListComponent implements OnInit {

  disciplines: Array<Discipline>;
  selectedDiscipline: Discipline;


  constructor(private disciplineService: DisciplineService) {
  }

  ngOnInit(): void {
    this.disciplineService.getDisciplines()
      .subscribe(disciplines => this.disciplines = disciplines);
  }

  onSelect(discipline: Discipline): void {
    this.selectedDiscipline = discipline;
  }

  gotoDetails(): void {
    console.log("gotoDetails");
  }
}
