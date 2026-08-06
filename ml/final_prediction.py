from predict_ast import predict_ast
from breathing import analyze_breathing
from highlight_segments import detect_segments


def final_prediction(audio_path):

    ast_result = predict_ast(audio_path)

    breathing_result = analyze_breathing(audio_path)

    segment_result = detect_segments(audio_path)

    result = {

        "prediction": ast_result["prediction"],

        "confidence": ast_result["confidence"],

        "breathing": breathing_result,

        "segments": segment_result

    }

    return result


if __name__ == "__main__":

    audio_path = input("Enter Audio Path : ")

    result = final_prediction(audio_path)

    print("\n==============================")
    print(" FINAL PREDICTION ")
    print("==============================")

    print(result)

    print("==============================")