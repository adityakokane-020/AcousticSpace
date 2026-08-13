from predict_ast import predict_ast
from breathing import analyze_breathing
from breathing_alignment import analyze_alignment
from highlight_segments import detect_segments


def final_prediction(audio_path):

    # AST Prediction
    ast_result = predict_ast(audio_path)

    # Breathing Analysis
    breathing_result = analyze_breathing(audio_path)

    # Breathing-Speech Alignment
    alignment_result = analyze_alignment(audio_path)

    # Suspicious Segments
    segment_result = detect_segments(audio_path)

    # Final Result
    result = {

        "prediction": ast_result["prediction"],

        "confidence": ast_result["confidence"],

        "breathing": breathing_result,

        "alignment": alignment_result,

        "segments": segment_result

    }

    return result


if __name__ == "__main__":

    audio_path = input(
        "Enter Audio Path : "
    )

    result = final_prediction(
        audio_path
    )

    print("\n==============================")
    print(" FINAL PREDICTION ")
    print("==============================")

    print(result)

    print("==============================")