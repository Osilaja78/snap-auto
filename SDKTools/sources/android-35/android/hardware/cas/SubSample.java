/*
 * This file is auto-generated.  DO NOT MODIFY.
 * Using: out/host/linux-x86/bin/aidl --lang=java --structured --version 1 --hash bc51d8d70a55ec4723d3f73d0acf7003306bf69f --stability vintf --min_sdk_version current -pout/soong/.intermediates/hardware/interfaces/common/aidl/android.hardware.common_interface/2/preprocessed.aidl --ninja -d out/soong/.intermediates/hardware/interfaces/cas/aidl/android.hardware.cas-V1-java-source/gen/android/hardware/cas/SubSample.java.d -o out/soong/.intermediates/hardware/interfaces/cas/aidl/android.hardware.cas-V1-java-source/gen -Nhardware/interfaces/cas/aidl/aidl_api/android.hardware.cas/1 hardware/interfaces/cas/aidl/aidl_api/android.hardware.cas/1/android/hardware/cas/SubSample.aidl
 */
package android.hardware.cas;
/** @hide */
public class SubSample implements android.os.Parcelable
{
  public int numBytesOfClearData = 0;
  public int numBytesOfEncryptedData = 0;
  @Override
   public final int getStability() { return android.os.Parcelable.PARCELABLE_STABILITY_VINTF; }
  public static final android.os.Parcelable.Creator<SubSample> CREATOR = new android.os.Parcelable.Creator<SubSample>() {
    @Override
    public SubSample createFromParcel(android.os.Parcel _aidl_source) {
      SubSample _aidl_out = new SubSample();
      _aidl_out.readFromParcel(_aidl_source);
      return _aidl_out;
    }
    @Override
    public SubSample[] newArray(int _aidl_size) {
      return new SubSample[_aidl_size];
    }
  };
  @Override public final void writeToParcel(android.os.Parcel _aidl_parcel, int _aidl_flag)
  {
    int _aidl_start_pos = _aidl_parcel.dataPosition();
    _aidl_parcel.writeInt(0);
    _aidl_parcel.writeInt(numBytesOfClearData);
    _aidl_parcel.writeInt(numBytesOfEncryptedData);
    int _aidl_end_pos = _aidl_parcel.dataPosition();
    _aidl_parcel.setDataPosition(_aidl_start_pos);
    _aidl_parcel.writeInt(_aidl_end_pos - _aidl_start_pos);
    _aidl_parcel.setDataPosition(_aidl_end_pos);
  }
  public final void readFromParcel(android.os.Parcel _aidl_parcel)
  {
    int _aidl_start_pos = _aidl_parcel.dataPosition();
    int _aidl_parcelable_size = _aidl_parcel.readInt();
    try {
      if (_aidl_parcelable_size < 4) throw new android.os.BadParcelableException("Parcelable too small");;
      if (_aidl_parcel.dataPosition() - _aidl_start_pos >= _aidl_parcelable_size) return;
      numBytesOfClearData = _aidl_parcel.readInt();
      if (_aidl_parcel.dataPosition() - _aidl_start_pos >= _aidl_parcelable_size) return;
      numBytesOfEncryptedData = _aidl_parcel.readInt();
    } finally {
      if (_aidl_start_pos > (Integer.MAX_VALUE - _aidl_parcelable_size)) {
        throw new android.os.BadParcelableException("Overflow in the size of parcelable");
      }
      _aidl_parcel.setDataPosition(_aidl_start_pos + _aidl_parcelable_size);
    }
  }
  @Override
  public int describeContents() {
    int _mask = 0;
    return _mask;
  }
}
