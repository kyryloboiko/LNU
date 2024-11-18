import java.util.*;

public class Module_2 {
    public static void main(String[] args) {
        Car car1 = new Car("Toyota", 123, "japan beeeep");
        Car car2 = new Car("Honda", 456, "japan buuup");
        Car car3 = new Car("Ford", 789, "democratic beeeep");
        Car car4 = new Car("Chevrolet", 1011, "democratic buuup");
        Car car5 = new Car("BMW", 1213, "fashistic beeeep");
        Car car6 = new Car("Audi", 1415, "fashistic buuup");

        List<Car> carsList = new ArrayList<>();
        carsList.add(car1);
        carsList.add(car2); 
        carsList.add(car3);
        carsList.add(car4);
        carsList.add(car5); 
        carsList.add(car6);
        
        System.out.println("Original list: ");
        System.out.println(carsList);
        System.out.println();

        carsList.sort(Comparator.comparing(Car::getName));
        
        System.out.println("Sorted list: ");
        System.out.println(carsList);
        System.out.println();

        Set<Car> carsSet = new LinkedHashSet<>(carsList);
        
        System.out.println("Original set: ");
        System.out.println(carsSet);
        System.out.println();

        // Видалення 2 об’єктів з середини сету
        Iterator<Car> iterator = carsSet.iterator();
        int count = 0;
        while (iterator.hasNext()) {
            iterator.next();
            if (count == 2 || count == 3) {
                iterator.remove();
            }
            count++;
        }
        
        System.out.println("Set after removal: ");
        System.out.println(carsSet);
        System.out.println();

        // Помістити об’єкти у HashMap
        Map<String, Car> carsHashMap = new HashMap<>();
        for (Car car : carsSet) {
            carsHashMap.put(car.name + car.cheirNumber, car);
        }

        System.out.println("HashMap: ");
        System.out.println(carsHashMap);
        System.out.println();
    }
}
