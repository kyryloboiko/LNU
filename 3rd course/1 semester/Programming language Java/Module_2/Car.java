class Car {
    String name;
    int cheirNumber;
    String horn;

    public Car(String name, int cheirNumber, String horn) {
        this.name = name;
        this.cheirNumber = cheirNumber;
        this.horn = horn;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Car{name='" + name + "', cheirNumber=" + cheirNumber + ", horn='" + horn + "'}";
    }
}