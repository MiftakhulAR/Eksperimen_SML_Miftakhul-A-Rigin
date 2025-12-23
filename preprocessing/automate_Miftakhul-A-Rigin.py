import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(
    input_path: str,
    output_path: str
) -> None:
    """
    Fungsi untuk melakukan preprocessing data Heart Disease
    dan menyimpan dataset hasil preprocessing ke file CSV.
    """

    # Load dataset
    df = pd.read_csv(input_path)

    # Pisahkan fitur dan target
    X = df.drop('target', axis=1)
    y = df['target']

    # Scaling fitur numerik
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Konversi kembali ke DataFrame
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

    # Gabungkan kembali dengan target
    df_preprocessed = pd.concat(
        [X_scaled_df, y.reset_index(drop=True)],
        axis=1
    )

    # Simpan dataset hasil preprocessing
    df_preprocessed.to_csv(output_path, index=False)

    print("Preprocessing selesai. Dataset tersimpan di:", output_path)


if __name__ == "__main__":
    preprocess_data(
        input_path="heart_raw.csv",
        output_path="preprocessing/heart_preprocessed.csv"
    )
