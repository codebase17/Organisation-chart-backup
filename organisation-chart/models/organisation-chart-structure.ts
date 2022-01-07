//Data structure for Organisation-chart

export class OrganisationChartStructure {
    public employeeName!: string;
    public employeeId!: number;
    public checked!: boolean;
    public reportingManagerId!: number;
    public reportees!: OrganisationChartStructure[];
}


