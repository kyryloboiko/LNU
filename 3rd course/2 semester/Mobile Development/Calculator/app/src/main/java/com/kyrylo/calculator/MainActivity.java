package com.kyrylo.calculator;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import java.text.DecimalFormat;

public class MainActivity extends AppCompatActivity {

    private TextView resultTextView;
    private String currentNumber = "";
    private String previousNumber = "";
    private String currentOperator = "";
    private double memoryValue = 0;
    private boolean isNewNumber = true;
    private static final DecimalFormat DECIMAL_FORMAT = new DecimalFormat("0.############");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        resultTextView = findViewById(R.id.resultTextView);
        //set ориентации
        //setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
    }

    // Обробка натискання цифрових клавіш
    public void onNumberClick(View view) {
        if (isNewNumber) {
            currentNumber = "";
            isNewNumber = false;
        }
        String digit = ((Button) view).getText().toString();
        currentNumber = currentNumber + digit;
        resultTextView.setText(currentNumber);
    }

    // Обробка натискання клавіші десяткової коми
    public void onDecimalClick(View view) {
        if (isNewNumber) {
            currentNumber = "0";
            isNewNumber = false;
        }
        if (!currentNumber.contains(".")) {
            currentNumber = currentNumber + ".";
            resultTextView.setText(currentNumber);
        }
    }

    // Обробка натискання клавіші "C" (Clear)
    public void onClearClick(View view) {
        currentNumber = "";
        previousNumber = "";
        currentOperator = "";
        isNewNumber = true;
        resultTextView.setText("0");
    }

    // Обробка натискання клавіші "±" (Change sign)
    public void onChangeSignClick(View view) {
        if (currentNumber.length() > 0 && !currentNumber.equals("0")) {
            if (currentNumber.startsWith("-")) {
                currentNumber = currentNumber.substring(1);
            } else {
                currentNumber = "-" + currentNumber;
            }
            resultTextView.setText(currentNumber);
        }
    }

    // Обробка натискання клавіш операторів (+, -, *, /, ^)
    public void onOperatorClick(View view) {
        if (currentNumber.length() > 0) {
            if (!previousNumber.isEmpty() && !currentOperator.isEmpty()) {
                calculate();
            }
            previousNumber = currentNumber;
            currentOperator = ((Button) view).getText().toString();
            isNewNumber = true;
        }
    }

    // Обробка натискання клавіші "="
    public void onEqualClick(View view) {
        if (currentNumber.length() > 0 && !currentOperator.isEmpty()) {
            calculate();
            currentOperator = "";
            isNewNumber = true;
        }
    }

    // Виконання обчислень
    private void calculate() {
        double result = 0;
        double num1 = Double.parseDouble(previousNumber);
        double num2 = Double.parseDouble(currentNumber);

        switch (currentOperator) {
            case "+":
                result = num1 + num2;
                break;
            case "-":
                result = num1 - num2;
                break;
            case "*":
                result = num1 * num2;
                break;
            case "/":
                if (num2 == 0) {
                    Toast.makeText(this, "Ділення на нуль неможливе", Toast.LENGTH_SHORT).show();
                    currentNumber = "";
                    previousNumber = "";
                    currentOperator = "";
                    isNewNumber = true;
                    resultTextView.setText("0");
                    return;
                }
                result = num1 / num2;
                break;
            case "^":
                result = Math.pow(num1, num2);
                break;
        }
        currentNumber = DECIMAL_FORMAT.format(result);
        resultTextView.setText(currentNumber);
        previousNumber = "";
    }

    // Функції пам'яті (MC, MR, M+, M-)
    public void onMemoryClearClick(View view) {
        memoryValue = 0;
        Toast.makeText(this, "Пам'ять очищена", Toast.LENGTH_SHORT).show();
    }

    public void onMemoryRecallClick(View view) {
        currentNumber = DECIMAL_FORMAT.format(memoryValue);
        resultTextView.setText(currentNumber);
        isNewNumber = true;
    }

    public void onMemoryAddClick(View view) {
        if (currentNumber.length() > 0) {
            memoryValue += Double.parseDouble(currentNumber);
            Toast.makeText(this, "Додано в пам'ять: " + DECIMAL_FORMAT.format(memoryValue), Toast.LENGTH_SHORT).show();
        }
    }

    public void onMemorySubtractClick(View view) {
        if (currentNumber.length() > 0) {
            memoryValue -= Double.parseDouble(currentNumber);
            Toast.makeText(this, "Віднято з пам'яті: " + DECIMAL_FORMAT.format(memoryValue), Toast.LENGTH_SHORT).show();
        }
    }
}

